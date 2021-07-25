# papirus-temperature-displayer

A very simple Python script used to pull temperature and humidity data from an HTTP endpoint and update a 2.7" [PaPiRus e-link display](https://github.com/PiSupply/PaPiRus) that's attached to a Raspberry Pi.

It requires a file called `config.json` at the root of the repository...

```
{
    "url": "http://localhost:3000"
}
```

...that points to an endpoint that returns data in the following format:

```
{
    "outdoor": {
        "temperature": "17.8",
        "humidity": "35"
    },
    "indoor": {
        "temperature": "20.2",
        "humidity": "50"
    }
}
```

To configure it to update every minute between 08:00 and 23:59 with cron (so it's not updating in the middle of the night when it's entirely unnecessary):

```
* 8-23 * * * /home/pi/Source/papirus-temperature-displayer/displayer.py >/dev/null 2>&1
```

## Credits
The font [Pixellium](https://www.fontspace.com/pixellium-font-f30306) used in this project is licensed as Creative Commons (by-nd) Attribution No Derivatives.
