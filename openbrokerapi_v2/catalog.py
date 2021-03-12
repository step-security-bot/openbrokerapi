from typing import List, Dict, Optional

from pydantic import BaseModel, Extra


class ServiceMetadata(BaseModel):
    displayName: str
    imageUrl: str
    longDescription: str
    providerDisplayName: str
    documentationUrl: str
    supportUrl: str
    shareable: Optional[bool] = None

    class Config:
        extra = Extra.allow


class ServiceDashboardClient(BaseModel):
    redirect_uri: str
    id: str = None
    secret: str = None

    class Config:
        extra = Extra.allow


class ServicePlanCost(BaseModel):
    amount: Dict[str, float]
    unit: str

    class Config:
        extra = Extra.allow


class ServicePlanMetadata(BaseModel):
    displayName: str = None
    bullets: List[str] = None
    costs: List[ServicePlanCost] = None

    class Config:
        extra = Extra.allow


class Schemas(BaseModel):
    service_instance: Dict = None
    service_binding: Dict = None

    #TODO allowed to have kwargs?
    class Config:
        extra = Extra.allow


class ServicePlan(BaseModel):
    id: str
    name: str
    description: str
    metadata: ServicePlanMetadata = None
    free: bool = None
    bindable: bool = None
    schemas: Optional[Schemas] = None

    class Config:
        extra = Extra.allow
