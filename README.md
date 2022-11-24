# WTP Map

Show the live location of trams and buses in Warsaw on an interactive map.

## API Reference

This project makes use of https://api.um.warszawa.pl complete API documentation can be
found [here](https://api.um.warszawa.pl/files/9fae6f84-4c81-476e-8450-6755c8451ccf.pdf)

#### Get locations

```http
  GET https://api.um.warszawa.pl/api/action/busestrams_get/
```

| Parameter     | Type     | Description                       |
|:--------------|:---------|:----------------------------------|
| `apikey`      | `string` | **Required**. Your API key        |
| `resource_id` | `string` | **Required**. Resource identifier |
| `type`        | `number` | **Required**. Vehicle type        |
| `line`        | `number` | Filter by bus line                |
| `brigade`     | `number` | Filter by brigade number          |

| Vehicle type | Description |
|:-------------|:------------|
| `1`          | Bus         |
| `2`          | Tram        |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY` - api.um.warszawa.pl API key

`MAPBOX_TOKEN` - mapbox public token

