from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.zp4rker.basic.plugins.module_utils import calculator


def run_module():
	module_args = dict(
		x=dict(type='int', required=True),
		operation=dict(type='str', required=True, choices=['add', 'subtract', 'multiply', 'divide']),
		y=dict(type='int', required=True)
	)

	result = dict(
		changed=False,
		equation=None,
		answer=None
	)

	module = AnsibleModule(
		argument_spec=module_args,
		supports_check_mode=False
	)

	x = module.params['x']
	y = module.params['y']

	if module.params['operation'] == 'add':
		result['equation'] = '{} + {}'.format(x, y)
		result['answer'] = calculator.add(x, y)
	elif module.params['operation'] == 'subtract':
		result['equation'] = '{} − {}'.format(x, y)
		result['answer'] = calculator.subtract(x, y)
	elif module.params['operation'] == 'multiply':
		result['equation'] = '{} × {}'.format(x, y)
		result['answer'] = calculator.multiply(x, y)
	else:
		result['equation'] = '{} ÷ {}'.format(x, y)
		if y == 0:
			module.fail_json(msg='You cannot divide by zero!', equation=result['equation'])
		result['answer'] = calculator.divide(x, y)

	module.exit_json(**result)


def main():
	run_module()


if __name__ == '__main__':
	main()