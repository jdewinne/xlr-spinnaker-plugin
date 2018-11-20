# xlr-spinnaker-plugin

This is the integration between XL Release and Spinnaker.

[![Build Status][xlr-spinnaker-plugin-travis-image] ][xlr-spinnaker-plugin-travis-url]
[![Github All Releases][xlr-spinnaker-plugin-downloads-image] ]()

[xlr-spinnaker-plugin-travis-image]: https://travis-ci.org/jdewinne/xlr-spinnaker-plugin.svg?branch=master
[xlr-spinnaker-plugin-travis-url]: https://travis-ci.org/jdewinne/xlr-spinnaker-plugin
[xlr-spinnaker-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-spinnaker-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-spinnaker-plugin-downloads-image]: https://img.shields.io/github/downloads/jdewinne/xlr-spinnaker-plugin/total.svg

## Overview ##

The xlr-spinnaker-plugin is a XL Release plugin that allows to deploy, rollback, ... spinnaker apps using XL Release.

## Installation

+ Place the [latest](https://github.com/jdewinne/xlr-spinnaker-plugin/releases) released version under the `plugins/__local__` dir.

This plugin (1.x.x+) requires xlr 8.2+

## Types ##

+ `spinnaker.Server`: A `configuration.HttpConnection` used to deploy to spinnaker.
    + Check Connection