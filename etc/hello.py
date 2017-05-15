CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'python': '/usr/bin/python3.5',
    'args': (
        '--bind=0.0.0.0:8090',
        '--workers=16',
        '--timeout=60',
		'--log-level=debug',
        'hello:application',
    ),
}
