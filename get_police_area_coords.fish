for loc in (cat coords_police_areas.txt)
curl "https://maps.googleapis.com/maps/api/geocode/json?address=$loc" -s | jq '.results[0] | .address_components[0].long_name + (.geometry.location | ", \(.lat), " + "\(.lng)")';
end
