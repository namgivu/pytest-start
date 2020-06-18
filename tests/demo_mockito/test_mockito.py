class Test:

    def test_when_no_mock(self):
        from src.util.demo_mock import longlong_time_to_run
        v = longlong_time_to_run()  # will take VERY LONG to finish
        assert v==122


    def test_with_mock(self):
        from mockito import when
        from src.util import demo_mock

        # mock longlong_time_to_run() to return immediately 333
        # ref. mockito https://pypi.org/project/mockito/
        when(demo_mock).longlong_time_to_run().thenReturn(333)

        # after mocked, value returned as mockedvalue ie 333 not 122
        v = demo_mock.longlong_time_to_run()  # will take VERY LONG to finish

        assert v == 333
