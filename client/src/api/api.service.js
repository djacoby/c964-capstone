import { navigate } from 'svelte-routing';

import { getApiRoute } from './api-routes';
import { convertDate, roundTrafficValue } from '../util';


let token;
export let user = JSON.parse(localStorage.getItem('user')).user;

async function get(route) {
  if (localStorage.getItem('user')) {
    token = JSON.parse(localStorage.getItem('user')).token;
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
  localStorage.setItem('user', JSON.stringify(json));
  return {
    status: !res.ok,
  }
}

/**
 * Logout user 
 */
export const logout = () => {
  localStorage.removeItem('user');
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
  const forecast = await res.json();
  const mappedForecast = forecast.result.map((f) => {
    return {
      ds: convertDate(f.ds),
      yhat1: roundTrafficValue(f.yhat1),
    };
  });

  return new Promise((resolve, reject) => {
    resolve(mappedForecast);
  });
};
