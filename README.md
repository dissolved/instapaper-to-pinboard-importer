# Instapaper to Pinboard Importer
> A quick and dirty importer that is better than the default Pinboard importer.


## Installation

Clone this repo.

## How to Use

Python 3.8.0 was used at the time of creation, but this probably works with any relevantly recent version of Python (let's say 3.6.x and newer, or maybe even earlier, but you're on your own).

You'll need your Pinboard API token ([found here](https://pinboard.in/settings/password)). The script will prompt you for it unless the `PINBOARD_API_TOKEN` environment variable is set.

You'll also need your Instapaper export in CSV format. At the time of this writing, you could request this towards the bottom of [this page](https://www.instapaper.com/user). The script will prompt you for its path.

```
python import.py
```

## Release History

* 0.0.1
    * Works for me

## Meta

Ryan Sandridge – [@dissolved](https://twitter.com/dissolved)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Instapaper to Pinboard Importer</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/dissolved/instapaper-to-pinboard-importer" property="cc:attributionName" rel="cc:attributionURL">Ryan Sandridge</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

[https://github.com/dissolved](https://github.com/dissolved/)

## Contributing

1. Fork it (<https://github.com/dissolved/instapaper-to-pinboard-importer/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
