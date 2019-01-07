const { watch } = require('gulp')
const { argv } = require('yargs')
const run = require('gulp-run')

function runPython (directory) {
  return run('python ' + directory + '/main.py').exec()
}

function defaultTask () {
  const directory = argv.directory
  watch(directory + '/*.py', () => runPython(directory))
}

exports.default = defaultTask
