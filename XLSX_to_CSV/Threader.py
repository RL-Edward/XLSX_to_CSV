from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


class Threader:
    MAX_THREAD_WORKERS = 4
    @classmethod
    def threads(cls, job_dict):
        job_list = []
        for func, args in job_dict.items():
          for arg in args:
            job_list.append((func, arg))
        with ThreadPoolExecutor(max_workers=cls.MAX_THREAD_WORKERS) as executor:
            thread_result_list = []
            for job in job_list:
              thread_result_list.append(executor.submit(job[0], None, **job[1]))
        executor.shutdown()
        print(thread_result_list[0].result())
        return thread_result_list

          

class Processor:
    MAX_PROCESSES = 4
    @classmethod
    def processes(cls, func, args):
        with ProcessPoolExecutor(max_workers=cls.MAX_PROCESSES) as executor:
            future_list = {executor.submit(func, arg): arg for arg in args} # future list captures thread 'returns'
        executor.shutdown()
        our_list = []
        for future in future_list.keys():
            our_list.append(future.result())
        return our_list