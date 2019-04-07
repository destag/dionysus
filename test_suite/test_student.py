"""Tests for Student class."""
import pytest

from pathlib import Path
from unittest import TestCase

from dionysus_app.student import Student


@pytest.fixture()
def test_student_name_only():
    test_name = 'Arthur, King of the Britons'
    yield Student(test_name)


@pytest.fixture()
def test_student_with_avatar_path():
    test_name = 'Arthur, King of the Britons'
    test_avatar_path = Path(r'path\to\avatar\for\Arthur')
    yield Student(name=test_name, avatar_path=test_avatar_path)


class TestStudentName:
    """
    Test Student name and path_safe_name properties.
    """

    def setup_method(self):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """

        self.test_name = 'Arthur, King of the Britons'

        self.test_changed_name = 'Sir Lancelot: the not-so-brave'

    def test_name_getter(self, test_student_name_only):
        assert test_student_name_only.name == self.test_name

    def test_name_setter_unmocked(self, test_student_name_only):
        assert test_student_name_only.name != self.test_changed_name

        # Change name
        test_student_name_only.name = self.test_changed_name

        assert test_student_name_only.name == self.test_changed_name

    @pytest.mark.parametrize(
        'name_arg',
        [{'passing a dict': 'Some value'},  # dict
         ['passing', 'a', 'list'],  # list
         Student('Student object for name'),  # Student object
         ('passed', 'tuple',),  # tuple
         ])
    def test_non_str_name_raises_error(self, name_arg):
        """Test error is raised for each bad type, error msg contains type."""
        with pytest.raises(TypeError, match=str(type(name_arg))):
            Student(name=name_arg)


class TestStudentNameMocked(TestCase):
    def setUp(self):
        self.test_name = 'Arthur, King of the Britons'

        self.test_student = Student(self.test_name)

        self.test_changed_name = 'Sir Lancelot: the not-so-brave'


class TestStudentAvatar:
    def setup_method(self):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        self.test_name = 'Arthur, King of the Britons'
        self.test_avatar_path_str = 'camelot'
        self.test_avatar_path_path = Path('camelot')

    def test_no_avatar_on_instantiation(self, test_student_name_only):
        assert test_student_name_only.avatar_path is None

    def test_change_avatar_passing_str(self, test_student_name_only):
        assert test_student_name_only.avatar_path != self.test_avatar_path_path

        test_student_name_only.avatar_path = self.test_avatar_path_path

        assert isinstance(test_student_name_only.avatar_path, Path)
        assert test_student_name_only.avatar_path == self.test_avatar_path_path

    def test_change_avatar_passing_path(self, test_student_name_only):
        assert test_student_name_only.avatar_path != self.test_avatar_path_path

        test_student_name_only.avatar_path = self.test_avatar_path_path

        assert isinstance(test_student_name_only.avatar_path, Path)
        assert test_student_name_only.avatar_path == self.test_avatar_path_path

    # Test instantiate with avatar_path:

    def test_instantiate_with_avatar_path_str(self):
        test_instantiate_student_with_avatar = Student(self.test_name,
                                                       avatar_path=self.test_avatar_path_str)

        assert test_instantiate_student_with_avatar.avatar_path == self.test_avatar_path_path

        assert isinstance(test_instantiate_student_with_avatar.avatar_path, Path)

    def test_instantiate_with_avatar_path_path(self):
        test_instantiate_student_with_avatar = Student(self.test_name,
                                                       avatar_path=self.test_avatar_path_path)

        assert test_instantiate_student_with_avatar.avatar_path == self.test_avatar_path_path

        assert isinstance(test_instantiate_student_with_avatar.avatar_path, Path)


class TestStudentJsonDict:
    @pytest.mark.parametrize(
        'student_object,output_json',
        [(Student('Sir Galahad'), {'name': 'Sir Galahad'}),  # name only
         (Student('Sir Lancelot: the Brave', avatar_path=None), {'name': 'Sir Lancelot: the Brave'}),
         # use str(Path()) to be sys agnostic.
         (Student('Arther, King of the Britons', avatar_path='Holy\\Grail'),
          {'name': 'Arther, King of the Britons', 'avatar_path': str(Path('Holy\\Grail'))}
          ),
         (Student('Brian', avatar_path=Path('a\\naughty\\boy')),
          {'name': 'Brian', 'avatar_path': str(Path('a\\naughty\\boy'))}),
         ])
    def test_json_dict(self, student_object, output_json):
        assert student_object.json_dict() == output_json


class TestStudentFromDict:
    @pytest.mark.parametrize(
        'output_json_dict',
        [({'name': 'Sir Galahad'}),  # name only
         ({'name': 'Sir Lancelot: the Brave'}),
         # use str(Path()) to be sys agnostic.
         ({'name': 'Arther, King of the Britons', 'avatar_path': str(Path('Holy\\Grail'))}),
         ({'name': 'Brian', 'avatar_path': str(Path('a//naughty//boy'))}),
         ])
    def test_from_dict(self, output_json_dict):
        student_object = Student.from_dict(output_json_dict)
        assert isinstance(student_object, Student)
        # Verify instantiated object is equivalent by reserialising:
        assert student_object.json_dict() == output_json_dict

        # Test attributes
        assert student_object.name == output_json_dict['name']
        if output_json_dict.get('avatar_path') is not None:
            assert str(student_object.avatar_path) == output_json_dict['avatar_path']


class TestStudentRepr:
    @pytest.mark.parametrize('student_object',
                             [Student(name='I have no avatar!'),
                              Student(name='I have an avatar', avatar_path='path_to_my_avatar'),
                              ])
    def test_repr(self, student_object):
        assert repr(student_object) == (f'{student_object.__class__.__module__}'
                                        f'.{student_object.__class__.__name__}('
                                        f'name={student_object._name!r}, '
                                        f'avatar_path={student_object._avatar_path!r})')


class TestStudentStr:
    @pytest.mark.parametrize('student_object, expected_str',
                             [(Student(name='I have no avatar!'), f"Student {'I have no avatar!'}, with no avatar."),
                              (Student(name='I have an avatar', avatar_path='path_to_my_avatar'), (f"Student {'I have an avatar'}, "
                                                                                                   f"with avatar {'path_to_my_avatar'}.")),
                              ])
    def test_str(self, student_object, expected_str, test_student_name_only, test_student_with_avatar_path):
        assert str(student_object) == expected_str