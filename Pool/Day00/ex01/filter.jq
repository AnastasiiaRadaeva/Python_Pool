.items | map({id, created_at, name, has_test, alternate_url}) | (first | keys_unsorted) as $keys | map([to_entries[] | .value]) as $rows | $keys,$rows[] | @csv
