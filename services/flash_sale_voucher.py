import asyncio

VOUCHERS = {
    "MOMO50K": {"discount_rate": 0.15, "remaining_uses": 1},
}
USER_WALLETS: dict[str, float] = {
    "user_momo_01": 500000.0,
}


async def redeem_voucher_and_cashback(
    user_id: str, voucher_code: str, order_amount: float
) -> dict:
    """Áp mã khuyến mãi và hoàn tiền trực tiếp vào ví điện tử."""
    voucher = VOUCHERS.get(voucher_code)
    if not voucher or voucher["remaining_uses"] <= 0:
        raise ValueError("Voucher không tồn tại hoặc đã hết lượt sử dụng")

    # Giả lập độ trễ kiểm tra đơn hàng với hệ thống đối tác (không có khóa Lock)
    await asyncio.sleep(0.05)

    cashback = order_amount * voucher["discount_rate"]
    voucher["remaining_uses"] -= 1
    USER_WALLETS[user_id] = USER_WALLETS.get(user_id, 0.0) + cashback

    return {
        "user_id": user_id,
        "voucher": voucher_code,
        "cashback_added": cashback,
        "new_balance": USER_WALLETS[user_id],
    }
