class Test:

    def test_when_no_mock(self):
        from src.util2.demo_mock2 import longlong_time_to_run
        v = longlong_time_to_run(s='sss')  # will take VERY LONG to finish
        assert v=='s=sss s2=122'


    def test_with_mock(self):

        #region do mocking
        from mockito import when
        from mockito import unstub

        #from src.util2 import another_module; when(another_module).another_module_method().thenReturn(333)  #NOTE mocking this way will not work when run together with other test methods; run it alone is fine
        from src.util2 import demo_mock2; when(demo_mock2).another_module_method().thenReturn(333)           #NOTE this works all the time; number1thumb rule is to mock with module-path in where the method is imported, NOT the method definition
        #endregion

        # testee code
        from src.util2.demo_mock2 import longlong_time_to_run
        v = longlong_time_to_run(s='sss')  # will take VERY LONG to finish
        assert v == 's=sss s2=333'

        # MUST reset mock when ending
        unstub()
