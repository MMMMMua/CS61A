test = {
  'name': 'Structure',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'e7df6bc0dc456d2631ac280dcebe1e2d',
          'choices': [
            'tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])',
            'tree(1, (tree(2), tree(3, (tree(5))), tree(5)))',
            'tree(2, [tree(1, tree(3, tree(5)))], tree(4))',
            'tree(1, [tree(2), tree(3), tree(4)], tree(5))'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which constructor call creates the following tree structure?
              1
            / | \
           2  3  4
             /
            5
          """
        },
        {
          'answer': 'ee4ae32605fa286b61abc4995ff7b5d6',
          'choices': [
            'tree(3, [tree(6, [tree(2), tree(1)]), tree(2), tree(7)])',
            'tree(3, tree(6, [tree(2), tree(1)]), tree(2), tree(7))',
            'tree(3, [tree(6), [tree(2), tree(1)], tree(2), tree(7)])',
            'tree(3, tree(6), [tree(2), tree(1)], [tree(2), tree(7)])'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which constructor call creates the following tree structure?
                3
              / | \
             6  2  7
            / \
           2   1
          """
        },
        {
          'answer': '31f02e75f8bef5a0621b68131795447b',
          'choices': [
            '2',
            '3',
            '6',
            '7'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many children does the following tree have?
                7
               / \
              2  4
             /|  |
            1 5  2
              |
              3
          """
        },
        {
          'answer': 'b87929dc6098331f794e03405a9c6e64',
          'choices': [
            '1, 6, 5',
            '1, 6, 5, 4',
            '7, 6, 1, 5, 4',
            'None of the above'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Given the following tree structure, what are all the leaves?
                7
              / | \
             3  2  4
            /  /|
           6  1 5
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
