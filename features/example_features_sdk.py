# read a JSON file that holds a list of bundles
# feed that into the features SDK to get a list of features

from google.protobuf import json_format

from moonsense.models import SealedBundle
from moonsense_features import generate


def main():
  sealed_bundles = []
  bundles = []
  # read the JSON file
  with open('data/2023-05-03-0236-ChQvbbFg6fGiKt9Yikybng-bundles.json') as f:
      raw_bundles = f.readlines()
      for raw_bundle in raw_bundles:
          # convert the JSON to a SealedBundle
          sealed_bundle = json_format.Parse(raw_bundle, SealedBundle(), ignore_unknown_fields=True)

          bundles.append(sealed_bundle.bundle)
          sealed_bundles.append(sealed_bundle)
  

  # generate the features
  features = generate(bundles)

  # features holds three types of features: behavioral, sdk and target_element
  # behavioral represents various behavioral features extracted from the list of bundles that was passed in
  # sdk represents an aggregation of the client-side SDK features
  # target_element represents the features for fields that have a target-element present

  # For the given session we only have behavioral features
  print("Available behavioral features", features.behavioral.keys())

  # For an example features named: pointer-mouse_left_button_dwell_time - it holds a double map with varios statistics
  print(features.behavioral['pointer-mouse_left_button_dwell_time'])
  # The available statistic for this feature are: count, max, min, mean, median, stdev.
  # Here's an example of how to access the mean value.
  print(features.behavioral['pointer-mouse_left_button_dwell_time'].double_map.value['mean'])

if __name__ == "__main__":
    main()