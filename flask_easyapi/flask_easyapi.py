from functools import partial
from functools import wraps
from typing import Callable

from flask import Blueprint
from flask import request


class EasyAPI(Blueprint):
    """
    EasyAPI is an object that makes defining a collection of related rest-api easier.

    Represents a collection of related rest-api routes that
    can later be registered on a real application.

    :param name: The name of the blueprint. Will be prepended to each
        endpoint name.
    :param import_name: The name of the blueprint package, usually
        ``__name__``. This helps locate the ``root_path`` for the
        blueprint.

    **Keyword arguments passed to Blueprint**

    See `flask Blueprint api
    <https://flask.palletsprojects.com/en/1.1.x/api/#blueprint-objects>`_
    for up-to-date information. The following is an extract of docs under
    `BSD-3-Clause License
    <https://github.com/pallets/flask/blob/master/LICENSE.rst>`_:

    :param static_folder: A folder with static files that should be
        served by the blueprint's static route. The path is relative to
        the blueprint's root path. Blueprint static files are disabled
        by default.
    :param static_url_path: The url to serve static files from.
        Defaults to ``static_folder``. If the blueprint does not have
        a ``url_prefix``, the app's static route will take precedence,
        and the blueprint's static files won't be accessible.
    :param template_folder: A folder with templates that should be added
        to the app's template search path. The path is relative to the
        blueprint's root path. Blueprint templates are disabled by
        default. Blueprint templates have a lower precedence than those
        in the app's templates folder.
    :param url_prefix: A path to prepend to all of the blueprint's URLs,
        to make them distinct from the rest of the app's routes.
    :param subdomain: A subdomain that blueprint routes will match on by
        default.
    :param url_defaults: A dict of default values that blueprint routes
        will receive by default.
    :param root_path: By default, the blueprint will automatically this
        based on ``import_name``. In certain situations this automatic
        detection can fail, so the path can be specified manually
        instead.
    """

    def __init__(self, name: str, import_name: str, *args: list, **kwargs: dict):
        bp_kwargs = {
            "static_folder",
            "static_url_path",
            "template_folder",
            "url_prefix",
            "subdomain",
            "url_defaults",
            "root_path",
            "cli_group",
        }
        Blueprint.__init__(
            self,
            name,
            import_name,
            **{kw: kwargs[kw] for kw in kwargs.keys() & bp_kwargs}
        )
        self.args = args
        self.kwargs = {kw: kwargs[kw] for kw in kwargs.keys() - bp_kwargs}

    def route(self, rule: str, **options):
        """
        A decorator that is used to register an api endpoint
        and its handler. The decorated function will automatically
        receive the url parameters as kwargs.

        .. note::  As of v0.1.0 unlike Blueprint, :meth:`route` and
            :meth:`add_url_rule` behaves differently for EasyAPI,
            this difference is expected to disappear in later releases.

        :param rule: The URL rule as string. See `flask route registrations api
                    <https://flask.palletsprojects.com/en/
                    1.1.x/api/#url-route-registrations>`_

        **Keyword arguments passed to Blueprint**

        See `flask route api <https://flask.palletsprojects.com/en/1.1.x/
        api/#flask.Flask.route>`_ for up-to-date information.
        The following is an extract of docs under `BSD-3-Clause License
        <https://github.com/pallets/flask/blob/master/LICENSE.rst>`_:

        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods
                        is a list of methods this rule should be limited
                        to (``GET``, ``POST`` etc.).  By default a rule
                        just listens for ``GET`` (and implicitly ``HEAD``).
                        Starting with Flask 0.6, ``OPTIONS`` is implicitly
                        added and handled by the standard request handling.
        """

        def coalesce(multi_dict):
            return {
                key: values[0] if len(values) == 1 else values
                for key, values in multi_dict.lists()
            }

        route = partial(Blueprint.route, self)

        def api_decorator(func: Callable):
            @route(rule, **options)
            @wraps(func)
            def wrapper(*args, **kwargs):
                request_args = coalesce(request.args)
                endpoint_kwargs = {**request_args, **kwargs}
                return func(*args, **endpoint_kwargs)

            return wrapper

        return api_decorator
