('test_precisely',
 [('E402', 13, 4, 'module level import not at top of file', '    import matplotlib.pyplot as plt\n'),
  ('E402', 22, 4, 'module level import not at top of file', '    import numpy as np\n'),
  ('E501',
   6,
   83,
   'line too long (82 > 80 characters)',
   "   sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n"),
  ('E702',
   16,
   26,
   'multiple statements on one line (semicolon)',
   "    plt.plot([1, 2, 3, 4]); plt.ylabel('some numbers');\n"),
  ('E703', 16, 54, 'statement ends with a semicolon', "    plt.plot([1, 2, 3, 4]); plt.ylabel('some numbers');\n"),
  ('F821', 25, 4, "undefined name 'hist'", '    hist(np.random.randn(10000), 100)\n')],
 {'logical lines': 7, 'physical lines': 10, 'tokens': 92})
