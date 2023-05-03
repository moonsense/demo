from moonsense.models import SealedBundle
from moonsense.util import json_format

from moonsense_features import generate, aggregate


def main():
  # Each file represents a session. A session usually it's an interaction with an individual web page or a single
  # screen of a native app.
  # Most often there are multiple sessions that are all connected via an unique identifier.
  # We call that identifier a "journey_id".
  data_files = [
    'data/2023-05-03-0236-ChQvbbFg6fGiKt9Yikybng-bundles.json',
    'data/2023-05-03-1616-TvePbQevntni46CNXTUFPL-bundles.json'
  ]

  all_features = []

  for data_file in data_files:
    bundles = []
    # read the JSON file
    with open(data_file) as f:
        raw_bundles = f.readlines()
        for raw_bundle in raw_bundles:
            # convert the JSON to a SealedBundle
            sealed_bundle = json_format.Parse(raw_bundle, SealedBundle(), ignore_unknown_fields=True)
            bundles.append(sealed_bundle.bundle)
    # generate the features
    features = generate(bundles)
    # we are accumulating here just the behavioral features - this needs to be done per feature type
    all_features.append(features.behavioral)
  
  # aggregate the features from all sessions
  aggregated_features = aggregate(all_features)

  print("Available behavioral features", aggregated_features.keys())
  print(aggregated_features['pointer-mouse_left_button_dwell_time'])

if __name__ == "__main__":
    main()