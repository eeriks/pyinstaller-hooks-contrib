# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

hiddenimports = ["sentry_sdk.integrations.stdlib",
                 "sentry_sdk.integrations.excepthook",
                 "sentry_sdk.integrations.dedupe",
                 "sentry_sdk.integrations.atexit",
                 "sentry_sdk.integrations.modules",
                 "sentry_sdk.integrations.argv",
                 "sentry_sdk.integrations.logging",
                 "sentry_sdk.integrations.threading",
                 "sentry_sdk.integrations.django",
                 "sentry_sdk.integrations.flask",
                 "sentry_sdk.integrations.bottle",
                 "sentry_sdk.integrations.falcon",
                 "sentry_sdk.integrations.sanic",
                 "sentry_sdk.integrations.celery",
                 "sentry_sdk.integrations.rq",
                 "sentry_sdk.integrations.aiohttp",
                 "sentry_sdk.integrations.tornado",
                 "sentry_sdk.integrations.sqlalchemy"]
