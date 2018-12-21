import os, threading


def get_current_process_thread_id():
    p_id  = threading.get_ident() #TODO do we need this
    th_id = os.getpid()           #TODO this seem to be the process id as pytest printed; not a thread
    s     = f'p{p_id}_th{th_id}'
    return s
