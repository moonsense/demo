from moonsense.models import SealedBundle
from moonsense.util import json_format

from moonsense_features import generate, features_to_dataframe, FeaturesGroupWithKeys


def main():
  # Each file represents a session. A session usually it's an interaction with an individual web page or a single
  # screen of a native app.
  # Most often there are multiple sessions that are all connected via an unique identifier.
  # We call that identifier a "journey_id".
  data_files = [
    'data/2023-05-03-0236-ChQvbbFg6fGiKt9Yikybng-bundles.json',
    'data/2023-05-03-1616-TvePbQevntni46CNXTUFPL-bundles.json'
  ]

  all_features_with_key = []

  for data_file in data_files:
    bundles = []
    latest_sealed_bundle = None
    # read the JSON file
    with open(data_file) as f:
        raw_bundles = f.readlines()
        for raw_bundle in raw_bundles:
            # convert the JSON to a SealedBundle
            sealed_bundle = json_format.Parse(raw_bundle, SealedBundle(), ignore_unknown_fields=True)
            bundles.append(sealed_bundle.bundle)

            latest_sealed_bundle = sealed_bundle
    # generate the features
    features = generate(bundles)
    features_with_key = FeaturesGroupWithKeys(features, {"session_id": latest_sealed_bundle.session_id, "journey_id": latest_sealed_bundle.journey_id})
    # we are accumulating here just the behavioral features - this needs to be done per feature type
    all_features_with_key.append(features_with_key)
  
  # aggregate the features from all sessions
  output = features_to_dataframe(all_features_with_key)
  print(output.behavioral.head())
  # this should be empty since the loaded bundles don't have any SDK features
  print(output.sdk.head())
  print(output.target_elements.head())

if __name__ == "__main__":
    main()