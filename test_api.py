#!/usr/bin/env python
"""
Example exec module to test the Anker API for various methods or direct
endpoint requests with various parameters.
"""
# pylint: disable=duplicate-code

import asyncio
import json
import logging
import sys

from aiohttp import ClientSession

import common
from api import api

_LOGGER: logging.Logger = logging.getLogger(__name__)
_LOGGER.addHandler(logging.StreamHandler(sys.stdout))
# _LOGGER.setLevel(logging.DEBUG)    # enable for detailed API output
CONSOLE: logging.Logger = logging.getLogger("console")
CONSOLE.addHandler(logging.StreamHandler(sys.stdout))
CONSOLE.setLevel(logging.INFO)


async def main() -> None:
    """Create the aiohttp session and run the example."""
    CONSOLE.info("Testing Solix API:")
    try:
        async with ClientSession() as websession:
            # Update your account credentials in  api.credentials.py or directly in this file for testing
            # Both files are added to .gitignore to avoid local changes being comitted to git
            myapi = api.AnkerSolixApi(
                common.user(),
                common.password(),
                common.country(),
                websession,
                _LOGGER,
            )

            # show login response
            # new = await myapi.async_authenticate(restart=True)      # enforce new login data from server
            # new = await myapi.async_authenticate()                  # receive new or load cached login data
            # if new:
            #     CONSOLE.info("Received Login response:")
            # else:
            #     CONSOLE.info("Cached Login response:")
            # CONSOLE.info(json.dumps(myapi._login_response, indent=2))     # show used login response for API reqests

            # test site api methods

            await myapi.update_sites()
            await myapi.update_device_details()
            CONSOLE.info("System Overview:")
            CONSOLE.info(json.dumps(myapi.sites, indent=2))
            CONSOLE.info("Device Overview:")
            CONSOLE.info(json.dumps(myapi.devices, indent=2))

            # test api methods
            # CONSOLE.info(json.dumps(await myapi.get_site_list(), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_homepage(), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_bind_devices(), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_user_devices(), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_charging_devices(), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_auto_upgrade(), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_scene_info(siteId='efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_wifi_list(siteId='efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_solar_info(siteId='efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'), indent=2))   # json parameters unknown: site_id not sifficient, or works only with Anker Inverters?
            # CONSOLE.info(json.dumps(await myapi.get_device_parm(siteId="efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c",paramType="4"), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_power_cutoff(siteId="efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c",deviceSn="9JVB42LJK8J0P5RY"), indent=2))
            # CONSOLE.info(json.dumps(await myapi.get_device_load(siteId="efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c",deviceSn="9JVB42LJK8J0P5RY"), indent=2))

            # CONSOLE.info(json.dumps(await myapi.energy_analysis(siteId="efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c",deviceSn="9JVB42LJK8J0P5RY",rangeType="week",startDay=datetime.fromisoformat("2023-10-10"),endDay=datetime.fromisoformat("2023-10-10"),devType="solar_production"), indent=2))
            # CONSOLE.info(json.dumps(await myapi.energy_analysis(siteId="efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c",deviceSn="9JVB42LJK8J0P5RY",rangeType="week",startDay=datetime.fromisoformat("2023-10-10"),endDay=datetime.fromisoformat("2023-10-10"),devType="solarbank"), indent=2))
            # CONSOLE.info(json.dumps(await myapi.energy_daily(siteId="efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c",deviceSn="9JVB42LJK8J0P5RY",startDay=datetime.fromisoformat("2024-01-10"),numDays=10), indent=2))
            # CONSOLE.info(json.dumps(await myapi.home_load_chart(siteId='efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'), indent=2))
            # """

            # # test api endpoints directly
            # """
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["homepage"],json={})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["site_list"],json={})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["bind_devices"],json={})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["user_devices"],json={})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["charging_devices"],json={})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["get_auto_upgrade"],json={})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["site_detail"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["wifi_list"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["get_site_price"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["solar_info"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "device_sn": "9JVB42LJK8J0P5RY"})), indent=2)) # json parameters unknown: May need site_id and device_sn of inverter in system?
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["get_cutoff"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "device_sn": "9JVB42LJK8J0P5RY"})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["get_device_fittings"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "device_sn": "9JVB42LJK8J0P5RY"})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["get_device_load"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "device_sn": "9JVB42LJK8J0P5RY"})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["get_device_parm"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c', "param_type": "4"})), indent=2))
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["compatible_process"],json={})), indent=2))    # json parameters unknown
            # CONSOLE.info(json.dumps((await myapi.request("post", api._API_ENDPOINTS["home_load_chart"],json={"site_id": 'efaca6b5-f4a0-e82e-3b2e-6b9cf90ded8c'})), indent=2))

            # test api from json files
            # myapi.testDir(os.path.join(os.path.dirname(__file__), "examples", "example1"))
            # await myapi.update_sites(fromFile=True)
            # await myapi.update_device_details(fromFile=True)
            # CONSOLE.info(json.dumps(myapi.sites,indent=2))
            # CONSOLE.info(json.dumps(myapi.devices,indent=2))

    except Exception as exception:  # pylint: disable=broad-exception-caught
        CONSOLE.error("%s: %s", type(exception), exception)


# run async main
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as err:  # pylint: disable=broad-exception-caught
        CONSOLE.exception("%s: %s", type(err), err)
