from extras.scripts import *

from dcim.models import Site
from dcim.choices import SiteStatusChoices
from ipam.models import Prefix
from ipam.choices import PrefixStatusChoices


class DisableSite(Script):
    class Meta:
        name = "Disable site"

    site_name = ObjectVar(
        description="Site To Update",
        model=Site,
        required=True
    )

    def run(self, data, commit):

        # Update the site status

        site = Site.objects.get(name=data['site_name'])
        if (site.status == SiteStatusChoices.STATUS_RETIRED):

          for prefix in Prefix.objects.filter(site=data['site_name']):
              prefix.status=PrefixStatusChoices.STATUS_DEPRECATED
              prefix.save()
              self.log_success(f"Updated Status of Prexix {prefix}")
  
