from typing import Callable
from flask import Blueprint
from functools import wraps, partial


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

    See `flask api reference <https://flask.palletsprojects.com/en/1.1.x/api/#blueprint-objects>`_
    for up-to-date information. The following is an extract of docs under
    `BSD-3-Clause License <https://github.com/pallets/flask/blob/master/LICENSE.rst>`_:

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

    def api(self, rule: str, **options):
        route = partial(Blueprint.route, self)

        def api_decorator(func: Callable):
            @route(rule, **options)
            @wraps(func)
            def api_wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return api_wrapper

        return api_decorator
