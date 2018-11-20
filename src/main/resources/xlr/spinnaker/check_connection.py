from spinnaker import SpinnakerClient

x = SpinnakerClient(configuration['url'], configuration['username'], configuration['password'])
x.get_applications()