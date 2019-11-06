# mock method with patch()
ref. https://docs.python.org/3/library/unittest.mock.html#patch-methods-start-and-stop

## basic patch()
```python
from package import module

patcher = patch('package.module.ClassName')
original = module.ClassName

new_mock = patcher.start()
assert module.ClassName is not original
assert module.ClassName is new_mock

patcher.stop()
assert module.ClassName is original
assert module.ClassName is not new_mock
```

## within a test class
```python
class MyTest(TestCase):

    def setUp(self):
        self.patcher1   = patch('package.module.Class1')
        self.patcher2   = patch('package.module.Class2')
        self.MockClass1 = self.patcher1.start()
        self.MockClass2 = self.patcher2.start()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()

    def test_something(self):
        assert package.module.Class1 is self.MockClass1
        assert package.module.Class2 is self.MockClass2

MyTest('test_something').run()
```

## or even cleaner w/ .addCleanup() ie. we don't wait until tearDown() to call patcher.stop() but register it right away when start mocking 
```python
class MyTest(TestCase):

    def setUp(self):
        patcher        = patch('package.module.Class')
        self.MockClass = patcher.start()
        self.addCleanup( patcher.stopall() )

    def test_something(self):
        assert package.module.Class is self.MockClass
```


#TODO util :sentinel
ref. https://docs.python.org/3/library/unittest.mock.html#sentinel


# @patch() decorator
https://docs.python.org/3/library/unittest.mock-examples.html#patch-decorators

mock object
```python
original = SomeClass.attribute

@patch.object(SomeClass, 'attribute', sentinel.attribute)
def test():
    assert SomeClass.attribute == sentinel.attribute

test()                                 # inside test() SomeClass.attribute is mocked
assert SomeClass.attribute == original # outside of test(), it's normal as :orinal
```

mock variable of a module aka. module attribute
```python
@patch('package.module.attribute', sentinel.attribute)
def test():
    from package.module import attribute
    assert attribute is sentinel.attribute

test()
```

# mock chain calls
ref. TODO

the context
```
class Something:
    
    def __init__(self):
        self.backend = BackendProvider()
        
    def method(self):
        response = self.backend.get_endpoint('foobar').create_call('spam', 'eggs').start_call()
something = Something()
something.method()
```

and we want to mock the :backend so that .method() call will result as :mock_response
we can get there as mock setup as below
```
mock_response = Mock(spec=open)
mock_backend  = Mock()
mock_backend \
    .get_endpoint .return_value \
    .create_call  .return_value \
    .start_call   .return_value \
    = mock_response

something.backend = mock_backend
assert something.method() == mock_response
```


# more on mocking by namgivu
ref. https://github.com/namgivu/python-mock-start
ref. https://github.com/namgivu/mocking-FlaskSqlAlchemy
