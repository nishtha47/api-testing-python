import pytest
import time
import concurrent.futures
from utils.api_client import APIClient
from config.config import config

class TestPerformanceStable:
    """Stable performance tests using reliable endpoints only"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.jsonplaceholder_url = config.get_base_url('jsonplaceholder')
    
    @pytest.mark.performance
    @pytest.mark.stable
    def test_response_time_validation_stable(self):
        """TC_PERF_001: Response Time Validation - JSONPlaceholder Only"""
        endpoints = [
            f"{self.jsonplaceholder_url}/posts/1",  # GET single
            f"{self.jsonplaceholder_url}/posts",    # GET collection
        ]
        
        # Realistic timeouts for reliable service
        timeouts = [2.0, 3.0]
        
        for endpoint, max_time in zip(endpoints, timeouts):
            start_time = time.time()
            response = self.client.get(endpoint, timeout=10)
            response_time = time.time() - start_time
            
            assert response.status_code == 200
            assert response_time < max_time, f"Response time {response_time:.2f}s exceeds {max_time}s for {endpoint}"
            print(f"✅ {endpoint}: {response_time:.2f}s")
    
    @pytest.mark.performance
    @pytest.mark.stable
    def test_concurrent_request_handling_stable(self):
        """TC_PERF_002: Concurrent Request Handling - JSONPlaceholder Only"""
        url = f"{self.jsonplaceholder_url}/posts/1"  # Reliable endpoint
        
        def make_request():
            try:
                start_time = time.time()
                response = self.client.get(url, timeout=10)
                response_time = time.time() - start_time
                return response.status_code, response_time, None
            except Exception as e:
                return None, None, str(e)
        
        # Make reasonable concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(make_request) for _ in range(5)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        # Filter successful requests
        successful_results = [r for r in results if r[0] == 200]
        error_results = [r for r in results if r[2] is not None]
        
        # Validation points
        assert len(successful_results) >= 3, f"Too many failed requests: {len(error_results)} errors"
        
        response_times = [result[1] for result in successful_results]
        avg_time = sum(response_times) / len(response_times)
        
        print(f"✅ Concurrent: {len(successful_results)} successful, avg time: {avg_time:.2f}s")
        assert avg_time < 2.0, f"Average response time {avg_time:.2f}s too high"
    
    @pytest.mark.performance
    @pytest.mark.stable
    def test_pagination_performance_stable(self):
        """TC_PERF_003: Pagination Performance - JSONPlaceholder Only"""
        pages = [1, 2]  # Only 2 pages for consistency
        response_times = []
        
        for page in pages:
            url = f"{self.jsonplaceholder_url}/posts?_page={page}&_limit=5"
            
            start_time = time.time()
            response = self.client.get(url, timeout=10)
            response_time = time.time() - start_time
            response_times.append(response_time)
            
            assert response.status_code == 200
        
        # Very lenient consistency check
        max_time = max(response_times)
        min_time = min(response_times)
        
        # Allow for 500% variance - external APIs can be unpredictable
        assert max_time <= min_time * 6, f"Response times vary: min={min_time:.2f}s, max={max_time:.2f}s"
        print(f"✅ Pagination: times={[f'{t:.2f}s' for t in response_times]}")
    
    @pytest.mark.performance
    @pytest.mark.stable
    def test_stress_test_stable(self):
        """TC_PERF_004: Stress Test - JSONPlaceholder Only"""
        url = f"{self.jsonplaceholder_url}/posts/1"  # Most reliable endpoint
        
        def make_request():
            try:
                response = self.client.get(url, timeout=10)
                return response.status_code, None
            except Exception as e:
                return None, str(e)
        
        # Realistic load for external service
        success_count = 0
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(make_request) for _ in range(10)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        end_time = time.time()
        
        for status_code, error in results:
            if status_code == 200:
                success_count += 1
        
        total_requests = len(results)
        success_rate = (success_count / total_requests) * 100
        
        # Very lenient success rate for external services
        assert success_rate >= 70, f"Success rate {success_rate}% is below 70%"
        
        total_time = end_time - start_time
        assert total_time < 15, f"Total execution time {total_time}s exceeds 15 seconds"
        
        print(f"✅ Stress test: {success_rate}% success rate in {total_time:.2f}s")