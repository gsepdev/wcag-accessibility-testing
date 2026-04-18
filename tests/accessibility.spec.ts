import { test, expect } from '@playwright/test';

test.describe('Accessibility checks', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://projects.accesscomputing.uw.edu/au/before.html#');
  });

  test('keyboard navigation reaches interactive elements', async ({ page }) => {
    await page.keyboard.press('Tab');

    const focusedElement = page.locator(':focus');
    await expect(focusedElement).toBeVisible();
  });

  test('focused element is visible', async ({ page }) => {
    await page.keyboard.press('Tab');

    const focusedElement = page.locator(':focus');
    await expect(focusedElement).toBeVisible();
  });

  test('form inputs exist and are interactable', async ({ page }) => {
    const nameInput = page.locator('input[name="name"]');
    const emailInput = page.locator('input[name="email"]');
  
    await expect(nameInput).toBeVisible();
    await expect(emailInput).toBeVisible();
  
    await nameInput.fill('');
    await emailInput.fill('');
  
    await expect(nameInput).toHaveValue('');
  });
});