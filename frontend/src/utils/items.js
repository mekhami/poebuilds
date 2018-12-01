export function widthAndHeightForGroup (group) {
  switch (group) {
    case 'dagger':
      return { 'w': 1, 'h': 3 }
    case 'claw':
      return { 'w': 2, 'h': 2 }
    case 'axe':
      return {}
    case 'mace':
      return {}
    case 'scepter':
      return {}
    case 'onesword':
      return { 'w': 1, 'h': 3 }
    case 'wand':
      return { 'w': 1, 'h': 3 }
    case 'chest':
      return { 'w': 2, 'h': 3 }
    case 'bow':
      return { 'w': 2, 'h': 3 }
  }
}
