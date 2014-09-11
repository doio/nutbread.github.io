# Info
pages = [
	{
		"name": "264",
		"name_full": "x264 Video Encoding Tools",
		"description": "Easier x264 interaction with 32bit and 64bit processes",
		"info": "Command line application",
		"tags": [ "python", "x264", "ffmpeg", ],
		"color": "#e38939",
	},
	{
		"name": "ass",
		"name_full": "Advanced SubStation Alpha Python Library",
		"description": "Easy macro commands for modifying .ass files",
		"info": "Python library",
		"tags": [ "python", "library", "subtitles", ],
		"color": "#ebcd31",
	},
	{
		"name": "crx",
		"name_full": "Chrome Extension Building Tools",
		"description": "Tools to help compile a Chrome extension from a userscript",
		"info": "Command line application",
		"tags": [ "python", "userscript", "chrome", ],
		"color": "#4195dc",
	},
	{
		"name": "lan",
		"name_full": "Local Area Network File Sharing",
		"description": "A simple way to share files across a local area network",
		"info": "Command line application",
		"tags": [ "javascript", "node.js", ],
		"color": "#d73c9e",
	},
	{
		"name": "pyp",
		"name_full": "Python Preprocessor",
		"description": "Run python code inside files",
		"info": "Command line application",
		"tags": [ "c", "python", "windows", ],
		"color": "#7d09c7",
	},
	{
		"name": "t2m",
		"name_full": "Torrent to Magnet",
		"description": "Javascript implementation of magnet URI generation",
		"info": "Web application &amp; libraries",
		"tags": [ "javascript", "library", ],
		"color": "#30b194",
	},
	{
		"name": "uyt",
		"name_full": "Usable YouTube",
		"description": "Makes YouTube more usable",
		"info": "Web browser extension",
		"tags": [ "javascript", "userscript", "youtube", ],
		"color": "#e42b28",
	},
	{
		"name": "vsd",
		"name_full": "Virtual SD Card Tools",
		"description": "Easily create and manage virtual disks on Windows",
		"info": "Command line application",
		"tags": [ "python", "windows", ],
		"color": "#60bf20",
	},
];



pages.sort(key=lambda i: i["name"]);



def generate_region_tags(page):
	value = [];

	has_info = "info" in page;
	has_info = False;

	if (has_info):
		value.append(
			'<span class="region_description_text">{0:s}</span>'.format(page["info"])
		);

	if ("tags" in page and len(page["tags"]) > 0):
		value.append('<span class="region_description_tags">');

		if (has_info):
			value.append(' &bull; ');

		for i in range(len(page["tags"])):
			tag = page["tags"][i];

			if (i > 0):
				value.append(' &bull; ');

			value.append('<a class="region_description_tag"><span>{0:s}</span></a>'.format(tag));

		value.append('</span>');

	return "".join(value);

