/**
 * Convert date from ISOstring to MM/DD/YYYY format
 */
export const convertDate = (date) => {
  return new Date(date).toLocaleString('en-us', {
    month: '2-digit',
    day: '2-digit',
    year: 'numeric',
  });
}

/**
 * Remove decimal places from a number
 * @param {number} trafficCount 
 */
export const roundTrafficValue = (trafficCount) => {
  return Math.round(Math.abs(trafficCount));
}
