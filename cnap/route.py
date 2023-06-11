routes = [ 
    #{"from_route": "/addresses", "to_route": "Address"},
	{
		"from_route": "/thematic-area/<docname>",
		"to_route": "/thematic-area/",
		#"defaults": {"doctype": "CNAP Thematic area", "parents": [{"label": "Addresses", "route": "addresses"}]},
	},
    {
		"from_route": "/service/<docname>",
		"to_route": "/service/",
	},

]