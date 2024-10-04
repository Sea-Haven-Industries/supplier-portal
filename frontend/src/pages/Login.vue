<template>
	<div class="m-3 flex flex-row items-center justify-center">
		<Card title="Welcome to Supplier Portal!" class="w-full max-w-md mt-4">
			<form class="flex flex-col space-y-2 w-full" @submit.prevent="submit">
				<Switch v-model="state.forAdmin" label="Login as Admin" />
				<div v-if="state.forAdmin">
					<Input
						required
						name="email"
						type="text"
						placeholder="username@email.com"
						label="User ID"
					/>
					<Input
						required
						name="password"
						type="password"
						placeholder="••••••"
						label="Password"
					/>
				</div>
				<div v-else>
					<Input
						required
						name="supplier_id"
						type="text"
						placeholder="Supplier ID"
						label="Supplier ID"
					/>
				</div>
				<Button :loading="session.login.loading" appearance="primary">Login</Button>
				<div v-if="session.login.error" class="text-red-500">
					{{ session.login.error }}
				</div>
			</form>
		</Card>
	</div>
</template>

<script lang="ts" setup>
import Switch from 'frappe-ui/src/components/Switch.vue'
import { reactive } from 'vue'
import { session } from '../data/session'
const state = reactive({
	forAdmin: false,
})

function submit(e) {
	let formData = new FormData(e.target)
	if (state.forAdmin) {
		session.login.submit({
			email: formData.get('email'),
			password: formData.get('password'),
		})
	} else {
		session.supplier_login.submit({
			supplier_id: formData.get('supplier_id'),
		})
	}
}
</script>
