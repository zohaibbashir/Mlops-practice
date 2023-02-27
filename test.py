from wallet import Wallet

wallet_obj = Wallet(10)

def test_total_amount_in_wallet():
  wallet_obj.addAmount(20)
  assert wallet_obj.getAmount() == 30
