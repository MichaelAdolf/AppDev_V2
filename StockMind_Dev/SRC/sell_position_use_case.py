from datetime import date, datetime
from uuid import uuid4

from stockmind.domain.portfolio.portfolio_trade import PortfolioTrade
from stockmind.infrastructure.portfolio.portfolio_repository import PortfolioRepository


class SellPositionUseCase:
    def __init__(self, database_path: str | None = None):
        self._repository = PortfolioRepository(database_path)

    def execute(self, position_id, sale_date, sale_price,
                sale_fees=0.0, tax_paid=0.0,
                exit_reason="MANUAL", note=""):
        position = self._repository.load_position(position_id)
        if position is None or position.status != "OPEN":
            raise ValueError("Offene Position wurde nicht gefunden.")
        if sale_price <= 0:
            raise ValueError("Verkaufspreis muss größer als 0 sein.")
        if sale_fees < 0 or tax_paid < 0:
            raise ValueError("Gebühren und Steuer dürfen nicht negativ sein.")

        purchase_day = date.fromisoformat(position.purchase_date)
        sale_day = date.fromisoformat(str(sale_date))
        if sale_day < purchase_day:
            raise ValueError("Verkaufsdatum darf nicht vor dem Kaufdatum liegen.")

        purchase_value = position.purchase_price * position.quantity
        sale_value = float(sale_price) * position.quantity
        gross_profit = sale_value - purchase_value
        profit_after_fees = gross_profit - position.purchase_fees - float(sale_fees)
        net_profit = profit_after_fees - float(tax_paid)
        gross_return_pct = gross_profit / purchase_value if purchase_value else 0.0
        invested_amount = purchase_value + position.purchase_fees
        net_return_pct = net_profit / invested_amount if invested_amount else 0.0
        now = datetime.now().isoformat(timespec="seconds")

        trade = PortfolioTrade(
            id=str(uuid4()), position_id=position.id, symbol=position.symbol,
            company_name=position.company_name, purchase_date=position.purchase_date,
            purchase_price=position.purchase_price, sale_date=str(sale_date),
            sale_price=float(sale_price), quantity=position.quantity,
            purchase_fees=position.purchase_fees, sale_fees=float(sale_fees),
            tax_paid=float(tax_paid), gross_profit=gross_profit,
            profit_after_fees=profit_after_fees, net_profit=net_profit,
            gross_return_pct=gross_return_pct, net_return_pct=net_return_pct,
            holding_days=(sale_day - purchase_day).days,
            entry_profile=position.entry_profile,
            entry_signal=position.entry_signal,
            entry_opportunity_score=position.entry_opportunity_score,
            exit_reason=exit_reason, note=note.strip(), created_at=now,
        )
        self._repository.close_position(position.id, now, trade)
        return trade
