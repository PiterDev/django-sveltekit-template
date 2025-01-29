import { BACKEND_API_URL } from '$env/static/private';

export const load = async ({ fetch }) => {
	const res = await fetch(BACKEND_API_URL + 'test/');
	const data = await res.json();

	return {
		data: data
	};
};
