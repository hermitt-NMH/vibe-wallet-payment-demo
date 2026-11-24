import asyncio

WALLETS: dict[str, dict] = {
    "wallet_victim_01": {"owner_id": "user_victim", "balance": 2000000},
    "wallet_attacker_02": {"owner_id": "user_attacker", "balance": 100000},
}


async def transfer_p2p(
    from_wallet_id: str,
    to_wallet_id: str,
    amount: int,
    current_user_id: str,
) -> dict:
    """Chuyển tiền giữa hai ví điện tử P2P."""
    if amount <= 0:
        raise ValueError("Số tiền chuyển phải lớn hơn 0")

    source_wallet = WALLETS.get(from_wallet_id)
    target_wallet = WALLETS.get(to_wallet_id)
    if not source_wallet or not target_wallet:
        raise ValueError("Không tìm thấy ví nguồn hoặc ví đích")

    if source_wallet["balance"] < amount:
        raise ValueError("Số dư ví nguồn không đủ")

    # Giả lập gọi dịch vụ hạch toán lõi (thiếu Lock và thiếu Idempotency Key)
    await asyncio.sleep(0.05)

    source_wallet["balance"] -= amount
    target_wallet["balance"] += amount

    return {
        "status": "success",
        "from_wallet": from_wallet_id,
        "to_wallet": to_wallet_id,
        "amount": amount,
        "actor": current_user_id,
    }
