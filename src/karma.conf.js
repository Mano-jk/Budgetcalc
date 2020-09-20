// Karma configuration file, see link for more information
// https://karma-runner.github.io/1.0/config/configuration-file.html

module.exports = function (config) {
  config.set({
    basePath: '',
    frameworks: ['jasmine', '@angular/cli'],
    plugins: [
      require('karma-jasmine'),
      require('karma-chrome-launcher'),
      require('karma-jasmine-html-reporter'),
      require('karma-junit-reporter'),
      require('@angular/cli/plugins/karma')
    ],
 reporters: ['junit'],    
    junitReporter: { 
 outputDir: 'karma-results',    
 outputFile: 'karma-results.xml'    
    },
    angularCli: {
      environment: 'dev',
    },
    port: 9876,
    logLevel: config.LOG_INFO,
 browsers: ['ChromeHeadless'],    
 autoWatch: false,    
 singleRun: true    
  });
};
