#!/usr/bin/env node
const program = require('commander');

program.version('v' + require('../package.json').version).description('版本');

program
  .command('install [name] [path]')
  .description('创建一个gulp项目')
  .action(function(name, path) {
    path = path || './';
    console.log(name, path);
  });

program
  .command('update')
  .description('update')
  .action(function() {
    console.log('update');
  });

program
  .command('remove')
  .description('remove')
  .action(function() {
    console.log('remove');
  });

program
  .command('add')
  .description('add')
  .action(function() {
    console.log('add');
  });

program
  .command('auth')
  .description('auth')
  .action(function() {
    console.log('auth');
  });

program
  .command('search [name]')
  .description('search by name')
  .action(function(name) {
    console.log('search' + name);
  });

program
  .command('open [name]')
  .description('open by name')
  .action(function(name) {
    console.log('open' + name);
  });

program
  .command('update ')
  .description('update')
  .action(function() {
    console.log('update');
  });

program.parse(process.argv);

if (program.args.length === 0) {
  program.help();
}
