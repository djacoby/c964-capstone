import { API_URL } from '../environments/environment';

/**
 * Api routes lookup object
 */
export const getApiRoute = {
  health: () => `${API_URL}/health`,
  store: () => `${API_URL}/store`,
  district: (districtId) => `${API_URL}/store/district/${districtId}`,
  singleStore: (storeId) => `${API_URL}/store/${storeId}`,
  forecast: (storeId, startDate, endDate) => {
    return `${API_URL}/store/${storeId}/forecast?start_date=${startDate}&end_date=${endDate}`;
  },
}
