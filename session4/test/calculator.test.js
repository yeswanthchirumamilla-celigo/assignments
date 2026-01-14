const { expect } = require('chai');
const calculator = require('../src/calculator');

describe('Calculator Unit Tests', () => {

  it('should add two numbers', () => {
    expect(calculator.add(2, 3)).to.equal(5);
  });

  it('should subtract two numbers', () => {
    expect(calculator.subtract(5, 3)).to.equal(2);
  });

  it('should multiply two numbers', () => {
    expect(calculator.multiply(4, 3)).to.equal(12);
  });

  it('should divide two numbers', () => {
    expect(calculator.divide(10, 2)).to.equal(5);
  });

  it('should throw error when dividing by zero', () => {
    expect(() => calculator.divide(10, 0))
      .to.throw('Division by zero');
  });

});
