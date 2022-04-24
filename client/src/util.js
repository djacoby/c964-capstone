/**
 * Convert date from ISOstring to MM/DD/YYYY format
 */
export const convertDate = (date) => {
  const d = date.replace(/\sGMT.*$/, "");
  return (new Date(d).toLocaleDateString());
}

/**
 * Remove decimal places from a number
 * @param {number} trafficCount 
 */
export const roundTrafficValue = (trafficCount) => {
  return Math.round(Math.abs(trafficCount));
}

/**
 * Get the starting date for date picker (tomorrows date)
 */
export const getStartDate = () => {
  const startDate = new Date();
  startDate.setDate(startDate.getDate() + 1);
  return convertToDateString(startDate);
}

/**
 * Get the ending date for date picker (seven days from today)
 */
export const getEndDate = () => {
  const endDate = new Date();
  endDate.setDate(endDate.getDate() + 7);
  return convertToDateString(endDate);
}

function convertToDateString(date) {
  return date.toISOString().split('T')[0];
}
