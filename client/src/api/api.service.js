import { navigate } from 'svelte-routing';

import { getApiRoute } from './api-routes';

export let token;

async function get(route) {
  if (localStorage.getItem('token')) {
    token = localStorage.getItem('token');
  }

  return fetch(route, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
}

async function post(route, body) {
  return fetch(route, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body)
  });
}

/**
 * Login user
 */
export const login = async (email, password) => {
  const route = getApiRoute.login();
  const res = await post(route, { email, password });
  const json = await res.json();
  localStorage.setItem('token', json['access_token']);
  return !res.ok;
}

/**
 * Logout user 
 */
export const logout = () => {
  localStorage.removeItem('token');
  token = '';
  navigate('/');
}


/**
 * Get store list from API
 */
export const getAllStoresList = async () => {
  const route = getApiRoute.store();
  const res = await get(route);
  return res.json();
};

/**
 * Get store list by district ID from API
 * 
 * @param {int} storeId 
 */
export const getStoreListByDistrict = async (districtId) => {
  const route = getApiRoute.district(districtId);
  const res = await get(route);
  return res.json();
};

/**
 * Get store by store ID from API
 * 
 * @param {int} storeId 
 */
export const getStoreById = async (storeId) => {
  const route = getApiRoute.singleStore(storeId);
  const res = await get(route);
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
  const res = await get(route);
  return res.json();
};
