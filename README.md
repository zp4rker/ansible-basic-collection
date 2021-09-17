# Ansible Basic Collection
A very basic collection simply designed to be used as a reference.

## Usage
### Setup
#### Setup directory structure
```mkdir ansible_collections/zp4rker/basic```
#### Clone repo
```
cd ansible_collections/zp4rker/basic
git clone https://github.com/zp4rker/ansible-basic-collection .
```

### Running tests
#### `print_time` role
```
ansible-test integration print_time_test
```
#### `calculate` module
```
ansible-test integration calculate
```
#### `calculator` module_utils unit test
```
ansible-test units tests/unit/plugins/module_utils/test_calculator.py
```