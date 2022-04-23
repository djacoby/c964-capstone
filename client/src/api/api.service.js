import { getApiRoute } from './api-routes';

/**
 * Get store list from API
 */
export const getAllStoresList = async () => {
  const route = getApiRoute.store();
  const res = await fetch(route);
  return res.json();
};

/**
 * Get store list by district ID from API
 * 
 * @param {int} storeId 
 */
export const getStoreListByDistrict = async (districtId) => {
  const route = getApiRoute.district(districtId);
  const res = await fetch(route);
  return res.json();
};

/**
 * Get store by store ID from API
 * 
 * @param {int} storeId 
 */
export const getStoreById = async (storeId) => {
  const route = getApiRoute.singleStore(storeId);
  const res = await fetch(route);
  return res.json();
};

/**
 * Get store forecast by store ID from API
 * 
 * @param {int} storeId 
 * @param {string} startDate
 * @param {string} endDate
 */
export const getForecast = async (storeId, startDate, endDate) => {
  const route = getApiRoute.forecast(storeId, startDate, endDate);
  const res = await fetch(route);
  return res.json();
};
