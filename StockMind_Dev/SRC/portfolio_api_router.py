from datetime import date
from dataclasses import asdict,is_dataclass
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
from stockmind.application.portfolio.add_position_use_case import AddPositionUseCase
from stockmind.application.portfolio.delete_portfolio_use_cases import DeletePositionUseCase,DeletePurchaseLotUseCase,DeleteTradeUseCase
from stockmind.application.portfolio.portfolio_dashboard_use_case import PortfolioDashboardUseCase
from stockmind.application.portfolio.portfolio_performance_use_case import PortfolioPerformanceUseCase
from stockmind.application.portfolio.sell_position_use_case import SellPositionUseCase
from stockmind.application.portfolio.update_purchase_lot_use_case import UpdatePurchaseLotUseCase
router=APIRouter(prefix='/portfolio',tags=['Portfolio'])
def d(v):
 if is_dataclass(v):return asdict(v)
 if isinstance(v,list):return[d(x) for x in v]
 if isinstance(v,dict):return{k:d(x) for k,x in v.items()}
 return v
class Add(BaseModel):symbol:str;purchase_date:date;purchase_price:float=Field(gt=0);quantity:float=Field(gt=0);purchase_fees:float=Field(0,ge=0);entry_profile:str='balanced';note:str=''
class Edit(BaseModel):purchase_date:date;purchase_price:float=Field(gt=0);quantity:float=Field(gt=0);purchase_fees:float=Field(0,ge=0);entry_profile:str='balanced';note:str=''
class Sell(BaseModel):sale_date:date;sale_price:float=Field(gt=0);sale_fees:float=Field(0,ge=0);tax_paid:float=Field(0,ge=0);exit_reason:str='MANUAL';note:str=''
@router.get('')
def portfolio():return d(PortfolioDashboardUseCase().load())
@router.get('/performance')
def performance():return PortfolioPerformanceUseCase().load()
@router.post('/positions')
def add(x:Add):
 try:return d(AddPositionUseCase().execute(**x.model_dump()))
 except ValueError as e:raise HTTPException(400,str(e))
@router.put('/lots/{lot_id}')
def edit(lot_id:str,x:Edit):
 try:return d(UpdatePurchaseLotUseCase().execute(lot_id=lot_id,**x.model_dump()))
 except ValueError as e:raise HTTPException(400,str(e))
@router.delete('/lots/{lot_id}')
def delete_lot(lot_id:str):DeletePurchaseLotUseCase().execute(lot_id);return{'status':'deleted'}
@router.delete('/positions/{position_id}')
def delete_position(position_id:str):DeletePositionUseCase().execute(position_id);return{'status':'deleted'}
@router.post('/positions/{position_id}/sell')
def sell(position_id:str,x:Sell):
 try:return d(SellPositionUseCase().execute(position_id=position_id,**x.model_dump()))
 except ValueError as e:raise HTTPException(400,str(e))
@router.delete('/trades/{trade_id}')
def delete_trade(trade_id:str):DeleteTradeUseCase().execute(trade_id);return{'status':'deleted'}
