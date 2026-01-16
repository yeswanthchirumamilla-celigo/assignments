const axios = require('axios')
require('dotenv').config()


const BASE_URL = 'https://api.integrator.io/v1'
const API_KEY = process.env.CELIGO_API_KEY
const CONNECTION_ID = '6967b0a570bb0d93bf28ef2c'

if (!API_KEY) {
  throw new Error('CELIGO_API_KEY env variable not set')
}

const client = axios.create({
  baseURL: BASE_URL,
  headers: {
    Authorization: `Bearer ${API_KEY}`,
    'Content-Type': 'application/json'
  }
})

async function createWebhookExport() {
  const res = await client.post('/exports', {
    name: 'listen webhook node',
    type: 'webhook',
    sandbox: false,
    webhook: {
      provider: 'custom',
      verify: 'basic',
      username: 'test',
      password: 'password',
      successStatusCode: 204,
      challengeSuccessBody: '{ "status": "success" }',
      challengeSuccessStatusCode: 200
    },
    adaptorType: 'WebhookExport'
  })
  return res.data._id
}

async function createHttpImport() {
  const res = await client.post('/imports', {
    name: 'mock api listener node',
    _connectionId: CONNECTION_ID,
    ignoreExisting: false,
    ignoreMissing: false,
    oneToMany: false,
    sandbox: false,
    http: {
      relativeURI: ['api/v1/users'],
      method: ['POST'],
      body: [],
      batchSize: 1,
      sendPostMappedData: true,
      isRest: false,
      formType: 'http'
    },
    adaptorType: 'HTTPImport'
  })
  return res.data._id
}

async function createFlow(exportId, importId) {
  const res = await client.post('/flows', {
    name: 'Webhook → Mock API Flow (Node)',
    disabled: false,
    runPageGeneratorsInParallel: true,
    autoResolveMatchingTraceKeys: true,
    pageGenerators: [
      { _exportId: exportId, skipRetries: false }
    ],
    pageProcessors: [
      {
        type: 'import',
        _importId: importId,
        responseMapping: { fields: [], lists: [] }
      }
    ]
  })
  return res.data._id
}

;(async () => {
  const exportId = await createWebhookExport()
  const importId = await createHttpImport()
  const flowId = await createFlow(exportId, importId)
  console.log({ exportId, importId, flowId })
})()
