export const addDays = (date, days) => {
	const result = new Date(date)
	result.setDate(result.getDate() + days)
	return result
}

export const parseInvoiceTerms = invoiceTerm => {
	switch (invoiceTerm) {
		case 'NET 10':
			return 10
		case 'NET 15':
			return 15
		case 'NET 30':
			return 30
		case 'NET 45':
			return 45
		case 'NET 60':
			return 60
		default:
			return 0
	}
}
