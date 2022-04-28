export const MIN_START_DATE = getStartDate();
export const END_DATE = getEndDate();

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
 * Validate that startDate is before MIN_START_DATE
 * 
 * @param {string} startDate
 */
export const validateStartDate = (startDate) => {
  const parsedMinStartDate = Date.parse(MIN_START_DATE);
  const parsedStartDate = Date.parse(startDate);

  return parsedStartDate >= parsedMinStartDate;
}

/**
 * Validate that startDate is before endDate
 * 
 * @param {string} startDate
 * @param {string} endDate
 */
export const validateEndDate = (startDate, endDate) => {
  const parsedStartDate = Date.parse(startDate);
  const parsedEndDate = Date.parse(endDate);

  return parsedStartDate < parsedEndDate;
}


/**
 * Get the starting date for date picker (tomorrows date)
 */
function getStartDate() {
  const startDate = new Date();
  startDate.setDate(startDate.getDate() + 1);
  return convertToDateString(startDate);
}

/**
 * Get the ending date for date picker (seven days from today)
 */
function getEndDate() {
  const endDate = new Date();
  endDate.setDate(endDate.getDate() + 7);
  return convertToDateString(endDate);
}

function convertToDateString(date) {
  return date.toISOString().split('T')[0];
}
