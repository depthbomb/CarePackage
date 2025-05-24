export type HttpClientOptions = {
	/**
	 * The name of this HTTP client.
	 */
	name: string;
	/**
	 * The base URL of requests the client makes.
	 */
	baseUrl?: string;
	/**
	 * The user agent to send with all requests from this client.
	 */
	userAgent: string;
	/**
	 * Whether to use a retry policy to retry failed requests.
	 */
	retry?: boolean;
	/**
	 *
	 */
	useQueue?: boolean;
	/**
	 *
	 */
	concurrency?: number;
	/**
	 *
	 */
	queueDelay?: number;
};
