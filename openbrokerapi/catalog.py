from typing import List, Dict, Optional


class ServiceMetadata:
    def __init__(
        self,
        displayName: str,
        imageUrl: str,
        longDescription: str,
        providerDisplayName: str,
        documentationUrl: str,
        supportUrl: str,
        shareable: Optional[bool] = None,
        **kwargs
    ):
        self.displayName = displayName
        self.imageUrl = imageUrl
        self.longDescription = longDescription
        self.providerDisplayName = providerDisplayName
        self.documentationUrl = documentationUrl
        self.supportUrl = supportUrl
        self.shareable = shareable

        self.__dict__.update(kwargs)


class ServiceDashboardClient:
    def __init__(self, *, id: str, secret: Optional[str] = None, redirect_uri: Optional[str]=None, **kwargs):
        self.id = id
        self.secret = secret
        self.redirect_uri = redirect_uri

        self.__dict__.update(kwargs)


class ServicePlanCost:
    def __init__(self, amount: Dict[str, float], unit: str, **kwargs):
        self.amount = amount
        self.unit = unit

        self.__dict__.update(kwargs)


class ServicePlanMetadata:
    def __init__(
        self,
        displayName: Optional[str] = None,
        bullets: Optional[List[str]] = None,
        costs: Optional[List[ServicePlanCost]] = None,
        **kwargs
    ):
        self.displayName = displayName
        self.bullets = bullets
        self.costs = costs

        self.__dict__.update(kwargs)


class Schemas:
    def __init__(
        self, service_instance: Optional[Dict] = None, service_binding: Optional[Dict] = None, **kwargs
    ):
        self.service_instance = service_instance
        self.service_binding = service_binding

        self.__dict__.update(kwargs)


class ServicePlan:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        metadata: Optional[ServicePlanMetadata] = None,
        free: Optional[bool] = None,
        bindable: Optional[bool] = None,
        schemas: Optional[Schemas] = None,
        **kwargs
    ):
        self.id = id
        self.name = name
        self.description = description
        self.metadata = metadata
        self.free = free
        self.bindable = bindable
        self.schemas = schemas

        self.__dict__.update(kwargs)
